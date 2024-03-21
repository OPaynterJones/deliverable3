import React from "react";
import "./ChooseYourInterestsPage.css";
import InterestGroup from "../../Components/InterestGroup/InterestGroup";

const ChooseYourInterestsPage = () => {
  const interests = ["Ball sports", "Digital sports", "Water Sports", "Team Sports", "Competitive Sports"];

  return <InterestGroup interestGroupName={"Sports"} interests={interests} />;
};

export default ChooseYourInterestsPage;
