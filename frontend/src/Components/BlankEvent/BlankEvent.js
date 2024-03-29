import React, { useState, useEffect } from "react";
import ColorThief from "colorthief";
import {
  BsHandThumbsUpFill,
  BsHandThumbsDownFill,
  BsArrowRepeat,
} from "react-icons/bs";

import "./BlankEvent.css";

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

const BlankEvent = ({ handleEventDataChange, societyName }) => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [eventData, setEventData] = useState({
    event_title: "",
    image: selectedImage,
    image_url: "",
    description: "",
    event_time: "",
    location: "",
  });
  const dominantColor = useDominantColor(eventData?.image_url);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setEventData({ ...eventData, [name]: value });
  };

  const handleImageChange = (event) => {
    const selectedFile = event.target.files[0];
    if (!selectedFile) return;

    setEventData({ ...eventData, image: selectedFile });
    const reader = new FileReader();
    reader.readAsDataURL(selectedFile);
    reader.onloadend = () => {
      setEventData({ ...eventData, imageUrl: reader.result });
    };
  };

  useEffect(() => {
    handleEventDataChange(eventData);
  }, [eventData]);

  useEffect(() => {
    console.log(eventData.image);
  }, [eventData]);

  return (
    <>
      <div className="event-card-container">
        <div
          className="event-card"
          style={{
            backgroundColor: dominantColor,
          }}
        >
          <input
            type="text"
            name="event_name"
            placeholder="Event title"
            className="input-event-title"
            value={eventData.title}
            onChange={handleInputChange}
          />
          {eventData.image_url ? (
            <img
              className="input-event-image"
              alt={"Event image name"}
              src={eventData.image_url}
            />
          ) : (
            <div className="image-upload">
              <input
                type="file"
                id="event-image"
                name="image"
                accept="image/*"
                onChange={(event) => {
                  setEventData({
                    ...eventData,
                    image: event.target.files[0],
                    image_url: URL.createObjectURL(event.target.files[0]),
                  });
                }}
              />
            </div>
          )}

          <div
            className="buttons"
            style={{ color: darkenColor(dominantColor, -0.85) }}
          >
            <BsHandThumbsUpFill size={65} />
            <BsArrowRepeat size={50} />
            <BsHandThumbsDownFill size={65} />
          </div>
          <textarea
            name="description"
            placeholder="Event description"
            className="input-event-description"
            value={eventData.description}
            onChange={handleInputChange}
          />
        </div>
      </div>
      <div className="additional-information">
        <div className="info-field">
          <h2 className="blank-society-name">{`${societyName} Society`}</h2>
        </div>
        <div className="info-field">
          <p className="blank-field-name">Time: </p>
          <input
            type="text"
            name="event_time"
            placeholder="Time"
            className="input-field"
            value={eventData.time}
            onChange={handleInputChange}
          />
        </div>
        <div className="info-field">
          <p className="blank-field-name">Location: </p>
          <input
            type="text"
            name="location"
            placeholder="Location"
            className="input-field"
            value={eventData.location}
            onChange={handleInputChange}
          />
        </div>
      </div>
    </>
  );
};

export default BlankEvent;
