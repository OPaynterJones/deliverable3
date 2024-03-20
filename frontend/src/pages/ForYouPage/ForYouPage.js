import React, { useEffect, useState } from "react";
import "./ForYouPage.css";
import ColorThief from "colorthief";
import {
  BsHandThumbsUpFill,
  BsHandThumbsDownFill,
  BsArrowRepeat,
} from "react-icons/bs";
import NavBar from "../../Components/NavBar/NavBar";

const darkenColor = (color, amount) => {
  if (!/^rgb\([0-9]{1,3}, [0-9]{1,3}, [0-9]{1,3}\)$/.test(color)) {
    return null;
  }

  const colorComponents = color
    .replace(/^rgb\(/, "")
    .replace(/\)$/, "")
    .split(", ")
    .map((component) => parseInt(component, 10));

  const darkenedComponents = colorComponents.map((component) => {
    const adjustedComponent = component * (1 - amount);
    return Math.max(0, Math.round(adjustedComponent));
  });

  return `rgb(${darkenedComponents.join(", ")})`;
};

const useDominantColor = (imageUrl) => {
  const [dominantColor, setDominantColor] = useState(null);

  useEffect(() => {
    if (!imageUrl) setDominantColor("rgb(26, 103, 148)");

    const img = new Image();
    img.crossOrigin = "Anonymous";
    img.onload = () => {
      const colorThief = new ColorThief();
      const color = colorThief.getColor(img);
      const darkenedColor = darkenColor(`rgb(${color.join(", ")})`, 0.45);
      setDominantColor(darkenedColor);
    };
    img.onerror = () => {
      setDominantColor("rgb(26, 103, 148)");
    };
    img.src = imageUrl;
  }, [imageUrl]);

  return dominantColor;
};

const getRecommendedEvent = async () => {
  try {
    const response = await fetch("http://localhost:5000/suggest_event", {
      credentials: "include",
    });
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching recommended event:", error);
  }
};

const ForYouPage = () => {
  const [eventData, setEventData] = useState(null);
  const [imageAnimation, setImageAnimation] = useState("initial");
  const dominantColor = useDominantColor(eventData?.image_url);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getRecommendedEvent();
        setEventData(data);
      } catch (error) {
        console.error("Error fetching random event:", error);
      }
    };

    fetchData();
  }, []);

  const handleInteract = (action) => {
    setImageAnimation(
      action === "like"
        ? "out-left"
        : action === "pass"
        ? "fade-out"
        : "out-right"
    );
    console.log(action);
    console.log(
      action === "like"
        ? "out-left"
        : action === "pass"
        ? "fade-out"
        : "out-right"
    );

    const animationPromise = new Promise((resolve) => setTimeout(resolve, 600));

    getRecommendedEvent()
      .then((data) => {
        return Promise.race([animationPromise]).then(() => data);
      })
      .then((data) => {
        setEventData(data);
        setImageAnimation("initial");
      })
      .catch((error) => console.error("Error fetching random event:", error));
  };

  return (
    <>
      <NavBar />
      <div className="for-you-page">
        <section className="splash-page">
          {
            <div className="Main">
              <h2 className="splashTitle">For You</h2>
              <h2
                className="splashInfo"
                style={{
                  left: "12vw",
                  top: "17vh",
                  fontSize: "2rem",
                  fontWeight: "500",
                }}
              >
                Get involved!
              </h2>
              <h2
                className="splashInfo"
                style={{
                  right: "12vw",
                  top: "32vh",
                  fontSize: "1.5rem",
                  textWrap: "break-word",
                  width: "50vw",
                }}
              >
                Our custom algorithm can help navigate all thats on offer at
                university
              </h2>
              <h2
                className="splashInfo"
                style={{ left: "17vw", top: "55vh", fontSize: "1.2rem" }}
              >
                Like and Dislike events below and let the Society Matchmaker
                guide you to your university community
              </h2>
              <h2
                className="splashInfo"
                style={{ top: "80vh", left: "45vw", fontSize: "0.9rem" }}
              >
                Continue below...
              </h2>
            </div>
          }
        </section>
        <section className="society-matchmaker">
          {eventData ? (
            <>
              <div className="event-container">
                <div
                  className="event-card"
                  style={{
                    backgroundColor: dominantColor,
                    transform: `${
                      imageAnimation === "out-left"
                        ? "translateX(-100px)"
                        : imageAnimation === "out-right"
                        ? "translateX(100px)"
                        : "translateX(0)"
                    }`,
                  }}
                >
                  <p className="event-title">{eventData.title}</p>
                  <img
                    className="event-image"
                    src={eventData.image_url}
                    alt={eventData.title}
                    style={{
                      opacity: imageAnimation !== "initial" ? 0.15 : 1,
                    }}
                  />

                  <div
                    className="buttons"
                    style={{ color: darkenColor(dominantColor, -0.85) }}
                  >
                    <BsHandThumbsUpFill
                      size={65}
                      onClick={() => handleInteract("like")}
                    />
                    <BsArrowRepeat
                      size={50}
                      onClick={() => handleInteract("pass")}
                    />

                    <BsHandThumbsDownFill
                      size={65}
                      onClick={() => handleInteract("dislike")}
                    />
                  </div>
                  <div className="event-description">
                    <p>{eventData.description}</p>
                  </div>
                </div>
                <div className="additional-information">
                  <p>{eventData.society_id}</p>
                  <p>Time: {eventData.time}</p>
                  <p>Location: {eventData.location}</p>
                </div>
              </div>
            </>
          ) : (
            <p>Loading event details...</p>
          )}
        </section>
      </div>
    </>
  );
};

export default ForYouPage;
