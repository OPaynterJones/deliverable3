import "./InterestGroup.css";
import React from "react";
import { useState, useEffect, useRef } from "react";
import Interest from "../Interest/Interest";

const InterestGroup = ({
  interestGroupName,
  interests,
  onSelectedInterestsChange,
}) => {
  const [selectedInterests, setSelectedInterests] = useState([]);
  const [isExpanded, setIsExpanded] = useState(false);
  const [circlePositions, setCirclePositions] = useState([]);
  const groupRef = useRef(null);

  const handleHover = () => {
    setIsExpanded(true);
  };

  const handleLeave = () => {
    setIsExpanded(false);
  };

  useEffect(() => {
    const calculateCirclePositions = (radius, numCircles) => {
      const angle = (2 * Math.PI) / numCircles;
      const positions = [];
      for (let i = 0; i < numCircles; i++) {
        const x = radius * Math.cos(i * angle - Math.PI / 2);
        const y = radius * Math.sin(i * angle - Math.PI / 2);
        positions.push({ x, y });
      }
      return positions;
    };

    if (interests.length > 0) {
      const radius = 158;
      setCirclePositions(calculateCirclePositions(radius, interests.length));
    }
  }, []);

  const handleSelectionChange = (interestName, isSelected) => {
    onSelectedInterestsChange(interestName, isSelected);
  };

  return (
    <div className="interest-group-container">
      <div
        ref={groupRef}
        className="boundary"
        onMouseEnter={handleHover}
        onMouseLeave={handleLeave}
        style={isExpanded ? { height: "500px", width: "500px" } : null}
      >
        <Interest isInterestGroupName={true} interestName={interestGroupName} />
        {interests.map((interestName, index) => (
          <Interest
            key={index}
            interestName={interestName}
            style={
              isExpanded
                ? {
                    transform: `translate(${circlePositions[index].x}px, ${circlePositions[index].y}px)`,
                    opacity: "1",
                  }
                : null
            }
            onSelectionChange={handleSelectionChange}
          />
        ))}
      </div>
    </div>
  );
};

export default InterestGroup;
