import React, { useState, useEffect } from "react";
import "./ChoseYourInterestsPage.css";
import InterestGroup from "../../Components/InterestGroup/InterestGroup";
import NavBar from "../../Components/NavBar/NavBar";
import { setUserInterests } from "../../api/setAPI";

const ChooseYourInterestsPage = () => {
  const [selectedInterests, setSelectedInterests] = useState([]);

  const handleSelectedInterestsChangeFromGroup = (
    interestName,
    wasSelected
  ) => {
    setSelectedInterests((prevSelectedInterests) =>
      wasSelected
        ? [...prevSelectedInterests, interestName]
        : prevSelectedInterests.filter((i) => i !== interestName)
    );
  };

  const handleSubmit = async () => {
    console.log("submitting", selectedInterests);
    try {
      const response = await setUserInterests(selectedInterests);
      console.log(response.message);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <>
      <NavBar title="Chose your interests" />
      <div className="row-container">
        <div className="interest-group-row">
          <div className="interest-group-container-container">
            <InterestGroup
              onSelectedInterestsChange={handleSelectedInterestsChangeFromGroup}
              interestGroupName={"Outdoor Activities"}
              interests={[
                "Racket / Bat Sport",
                "Strength",
                "Team",
                "Training",
                "Water Sport",
              ]}
            />
          </div>
          <div className="interest-group-container-container">
            <InterestGroup
              onSelectedInterestsChange={handleSelectedInterestsChangeFromGroup}
              interestGroupName={"Social & Entertainment"}
              interests={[
                "Acting",
                "Community",
                "Entertainment",
                "Games",
                "Pub",
                "Socialising",
                "Spectating",
              ]}
            />
          </div>
          <div className="interest-group-container-container">
            <InterestGroup
              onSelectedInterestsChange={handleSelectedInterestsChangeFromGroup}
              interestGroupName={"Arts & Performance"}
              interests={[
                "Art",
                "Creative",
                "Dance",
                "Design",
                "Film & TV",
                "Music",
                "Performance",
              ]}
            />
          </div>
          <div className="interest-group-container-container">
            <InterestGroup
              onSelectedInterestsChange={handleSelectedInterestsChangeFromGroup}
              interestGroupName={"Knowledge & Learning"}
              interests={[
                "Academic",
                "Business",
                "Data",
                "Debating",
                "Discussion",
                "History",
                "Law",
              ]}
            />
          </div>
          <div className="interest-group-container-container">
            <InterestGroup
              onSelectedInterestsChange={handleSelectedInterestsChangeFromGroup}
              interestGroupName={"Science & Technology"}
              interests={["Mathematics", "Politics", "Science", "Technology"]}
            />
          </div>
        </div>

        <div className="interest-group-row">
          <div className="interest-group-container-container">
            <InterestGroup
              onSelectedInterestsChange={handleSelectedInterestsChangeFromGroup}
              interestGroupName={"Sports"}
              interests={[
                "Ball Sport",
                "Combat",
                "Competitive",
                "Contact",
                "Fitness",
                "Health",
                "Running",
              ]}
            />
          </div>
          <div className="interest-group-container-container">
            <InterestGroup
              onSelectedInterestsChange={handleSelectedInterestsChangeFromGroup}
              interestGroupName={"Personal Growth"}
              interests={[
                "Fantasy",
                "Finance",
                "Food & Drink",
                "Inclusive",
                "Individual",
                "Indoors",
                "Relaxing",
              ]}
            />
          </div>
          <div className="interest-group-container-container">
            <InterestGroup
              onSelectedInterestsChange={handleSelectedInterestsChangeFromGroup}
              interestGroupName={"Global & Political"}
              interests={[
                "International Politics",
                "Internal Politics",
                "Religion",
              ]}
            />
          </div>
          <div className="interest-group-container-container">
            <InterestGroup
              onSelectedInterestsChange={handleSelectedInterestsChangeFromGroup}
              interestGroupName={"Entertainment & Tech"}
              interests={[
                "Public Speaking",
                "Roleplay",
                "Software",
                "Tabletop Games",
                "Technical",
                "Travel",
                "Videogames",
              ]}
            />
          </div>
        </div>

        <button className="submit-button" onClick={handleSubmit}>
          Confirm
        </button>
      </div>
    </>
  );
};

export default ChooseYourInterestsPage;
