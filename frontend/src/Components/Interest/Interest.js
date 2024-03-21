import "./Interest.css";
import React, { useEffect } from "react";
import { useState } from "react";

const Interest = ({
  isInterestGroupName,
  interestName,
  onSelectionChange,
  style,
}) => {
  const [isSelected, setIsSelected] = useState(false);

  useEffect(() => {
    if (isInterestGroupName) return;
    onSelectionChange(interestName, isSelected);
  }, [isSelected]);

  const handleClick = () => {
    setIsSelected(!isSelected);
  };

  return (
    <div
      className={!isInterestGroupName ? `interest` : `interest-group-name`}
      style={{
        ...style,
        border: isSelected ? "4px solid" : "1px solid",
      }}
      onClick={handleClick}
    >
      <span>{interestName}</span>
    </div>
  );
};

export default Interest;
