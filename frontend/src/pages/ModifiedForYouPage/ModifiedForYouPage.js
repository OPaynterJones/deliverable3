import React, { useEffect, useRef } from "react";
import styles from "./ModifiedForYouPage.module.css";
import NavBar from "../../Components/NavBar/NavBar";
import ModifiedEventContainer from "../../Components/ModifieidEventContainer/ModfiedEventContainer";
import { BsChevronDoubleUp } from "react-icons/bs";
import { IoReload } from "react-icons/io5";
import { useState } from "react";
import { modifyInterests } from "../../api/setAPI";
import { backendUrl } from "../../config";

const getRecommendedEvents = async () => {
  try {
    const response = await fetch(`${backendUrl}/recommend_event_group`, {
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

const ModifiedForYouPage = () => {
  const endOfGroupContainerRef = useRef(null);
  const [groups, setGroups] = useState([]);

  useEffect(() => {
    if (groups.length > 0) return;
    loadNewEvents();
  });

  const loadNewEvents = async () => {
    const newFetchedGroup = await getRecommendedEvents();
    if (!newFetchedGroup) return;
    setGroups([...groups, newFetchedGroup]);
  };

  useEffect(() => {
    endOfGroupContainerRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [groups]);

  const handleResponse = (eventId, action) => {
    console.log(`received ${action} from event id ${eventId}`);
    modifyInterests(eventId, action);
  };

  return (
    <>
      <div className={styles.forYouPage}>
        <NavBar />
        <div className={styles.scrollMessageContainer}>
          <BsChevronDoubleUp color="light blue" />
          <div className={styles.scrollMessage}>Previous </div>
        </div>
        <div className={styles.groupsContainer}>
          {groups.length > 0 ? (
            groups.map((group, index) => (
              <div key={index} className={styles.eventGroup}>
                {group.map((eventData, i) => (
                  <ModifiedEventContainer
                    key={i}
                    eventData={eventData}
                    handleResponse={handleResponse}
                  />
                ))}
              </div>
            ))
          ) : (
            <p>Loading new events...</p>
          )}
          <div ref={endOfGroupContainerRef} />
        </div>
        <div
          className={styles.scrollMessageContainerClickable}
          onClick={loadNewEvents}
        >
          <div className={styles.scrollMessage}>Load new events </div>
          <IoReload color="light blue" />
        </div>
      </div>
    </>
  );
};

export default ModifiedForYouPage;
