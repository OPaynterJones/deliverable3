import React, { useState } from "react";
import { BsHandThumbsUpFill, BsHandThumbsDownFill } from "react-icons/bs";
import styles from "./ModifiedEventContainer.module.css";

const ModifiedEventContainer = ({ eventData = null, handleResponse }) => {
  const [responseType, setResponseType] = useState(null);

  const handleButtonClick = (action) => {
    setResponseType(action);
    handleResponse(eventData.event_id, action);
  };

  return (
    <div className={styles.boundary}>
      <div className={styles.eventContainer}>
        <div className={styles.primaryInfoContainer}>
          <div className={styles.eventTitle}>
            {eventData?.event_name || "Event title TBD"}
          </div>
          <div className={styles.eventDescription}>
            {eventData?.description || "Event description TBD"}
          </div>
        </div>
        <div className={styles.secondaryInfoContainer}>
          <div className={styles.eventSociety}>
            {eventData?.society_name || "Society undetermined"}
          </div>
          <div className={styles.secondaryInfoField}>
            {eventData?.event_time || "Time TBD"}
          </div>
          <div className={styles.secondaryInfoField}>
            {eventData?.location || "Location TBD"}
          </div>
        </div>
        <img
          className={styles.eventImage}
          src={eventData?.image_filename}
          alt="Event"
        />
        <div className={styles.buttonContainer}>
          <BsHandThumbsUpFill
            size={60}
            onClick={() => handleButtonClick("like")}
            style={{
              cursor: "pointer",
              color: responseType === "like" ? "blue" : "black",
              opacity: responseType ? 0.5 : 1,
              pointerEvents: responseType ? "none" : "auto",
            }}
          />
          <BsHandThumbsDownFill
            size={60}
            onClick={() => handleButtonClick("dislike")}
            style={{
              cursor: "pointer",
              color: responseType === "dislike" ? "red" : "black",
              opacity: responseType ? 0.5 : 1,
              pointerEvents: responseType ? "none" : "auto",
            }}
          />
        </div>
      </div>
    </div>
  );
};

export default ModifiedEventContainer;