import React, { useState, useEffect } from "react";
import ColorThief from "colorthief";
import {
  BsHandThumbsUpFill,
  BsHandThumbsDownFill,
  BsArrowRepeat,
} from "react-icons/bs";
import { useNavigate } from "react-router-dom";
import "./EventContainer.css";
import { backendUrl } from "../../config";

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

const EventContainer = ({ incomingData = null, handleResponse }) => {
  const [timerRunning, setTimerRunning] = useState(false);
  const [eventData, setEventData] = useState(null);
  const dominantColor = useDominantColor(incomingData?.image_url);
  const navigate = useNavigate();

  const [animation, setAnimation] = useState("intial");

  const handleButtonClick = (action) => {
    if (!eventData) return;
    setAnimation(
      action === "like"
        ? "out-left"
        : action === "pass"
        ? "fade-out"
        : "out-right"
    );

    setTimerRunning(true);
    handleResponse(eventData.event_id, action);
  };

  useEffect(() => {
    if (!timerRunning) return;

    setTimeout(() => {
      setTimerRunning(false);
    }, 600);
  }, [timerRunning]);

  useEffect(() => {
    if (timerRunning) return;

    setEventData(incomingData);
    setAnimation("initial");
  }, [timerRunning, incomingData]);

  const goToSocietyPage = () => {
    if (eventData?.society_name) {
      navigate(`/societies/${eventData.society_name}`);
    }
  };

  return (
    <>
      <div className="event-card-container">
        <div
          className="event-card"
          style={{
            backgroundColor: dominantColor,
            transform: `${
              animation === "out-left"
                ? "translateX(-100px)"
                : animation === "out-right"
                ? "translateX(100px)"
                : "translateX(0)"
            }`,
          }}
        >
          <p className="event-title">{eventData?.event_name}</p>
          <img
            className="event-image"
            src={`${backendUrl}${eventData?.image_filename}` || ""}
            alt={eventData?.title || "No Title Available"}
            style={{
              opacity: animation !== "initial" ? 0.15 : 1,
            }}
          />
          <div
            className="buttons"
            style={{ color: darkenColor(dominantColor, -0.85) }}
          >
            <BsHandThumbsUpFill
              size={65}
              onClick={() => handleButtonClick("like")}
            />
            <BsArrowRepeat
              size={50}
              onClick={() => handleButtonClick("pass")}
            />
            <BsHandThumbsDownFill
              size={65}
              onClick={() => handleButtonClick("dislike")}
            />
          </div>
          <div className="event-description">
            {eventData?.description || "No Description Available"}
          </div>
        </div>
      </div>
      <div className="additional-information">
        <div className="info-field">
          <h2 className="society-name" onClick={goToSocietyPage}>
            {eventData ? `${eventData.society_name} Society` : "Society Name"}
          </h2>
        </div>
        <div className="info-field">
          <p className="field-name">Time: </p>
          <p className="field-info">{eventData?.event_time || "Time TBA"}</p>
        </div>
        <div className="info-field">
          <p className="field-name">Location: </p>
          <p className="field-info">{eventData?.location || "Location TBA"}</p>
        </div>
      </div>
    </>
  );
};

export default EventContainer;
