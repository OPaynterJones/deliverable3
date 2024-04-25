import React, { useEffect, useState } from "react";
import "./ForYouPage.css";
import NavBar from "../../Components/NavBar/NavBar";
import EventContainer from "../../Components/EventContainer/EventContainer";
import { checkSession } from "../../api/authAPI";
import BlankEvent from "../../Components/BlankEvent/BlankEvent";
import { backendUrl } from "../../config";

const getRecommendedEvent = async () => {
  try {
    const response = await fetch(`${backendUrl}/recommend_event`, {
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

  const [societyName, setSocietyName] = useState(null);
  const [isCreatingNewEvent, setIsCreatingNewEvent] = useState(false);
  const [newEventData, setNewEventData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await checkSession();
        setSocietyName(response.society_name);
      } catch {}
    };

    fetchData();
  }, []);

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
  };

  useEffect(() => {
    if (!newEventData || isCreatingNewEvent) return;

    const handleSaveEvent = async () => {
      try {
        const formData = new FormData();
        Object.keys({ ...newEventData, societyName }).forEach((key) => {
          console.log(key);
        });
        Object.keys({ ...newEventData }).forEach((key) => {
          console.log(key, newEventData[key]);
          formData.append(key, newEventData[key]);
        });

        formData.append("society_name", societyName);
        const response = await fetch(`${backendUrl}/create_new_event`, {
          method: "POST",
          credentials: "include",
          body: formData,
          enctype: "multipart/form-data",
        });

        if (!response.ok) {
          throw new Error(`HTTP error: ${response.status}`);
        }

        console.log("Event saved successfully!");
        setIsCreatingNewEvent(false);
      } catch (error) {
        console.error("Error saving event:", error);
      }
      setNewEventData(null);
    };

    handleSaveEvent();
  }, [isCreatingNewEvent]);

  return (
    <>
      <div className="for-you-page">
        <NavBar />
        <div className="page-content">
          {isCreatingNewEvent ? (
            <BlankEvent
              handleEventDataChange={setNewEventData}
              societyName={societyName}
            />
          ) : (
            <EventContainer
              incomingData={eventData}
              handleResponse={handleResponse}
            />
          )}
          {societyName && (
            <button
              className="create-new-event-button"
              onClick={() => setIsCreatingNewEvent(!isCreatingNewEvent)}
            >
              {isCreatingNewEvent ? "Save event" : "Create new event"}
            </button>
          )}
        </div>
      </div>
    </>
  );
};

export default ForYouPage;
