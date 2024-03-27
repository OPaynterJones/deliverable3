import React, { useEffect, useState } from "react";
import "./ForYouPage.css";
import NavBar from "../../Components/NavBar/NavBar";
import EventContainer from "../../Components/EventContainer/EventContainer";

const getRecommendedEvent = async () => {
  try {
    const response = await fetch("http://localhost:5000/recommend_event", {
      method: "GET",
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

  const handleResponse = (action) => {
    getRecommendedEvent().then(setEventData);
    //   .then((data) => {
    //     setEventData(data);
    //     setImageAnimation("initial");
    //   })
    //   .catch((error) => console.error("Error fetching random event:", error));
  };

  return (
    <>
      <div className="for-you-page">
        <NavBar />
        <div className="page-content">
          <EventContainer
            incomingData={eventData}
            handleResponse={handleResponse}
          />
          <div className="additional-information">
            <div className="info-field">
              <p className="field-name">Time: </p>
              <p className="field-info">{eventData?.time || "Time TBA"}</p>
            </div>
            <div className="info-field">
              <p className="field-name">Location: </p>
              <p className="field-info">
                {eventData?.location || "Location TBA"}
              </p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default ForYouPage;
