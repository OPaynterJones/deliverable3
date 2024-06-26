import React, { useState } from "react";
import "./ChooseYourInterestsPage.css";
import InterestGroup from "../../Components/InterestGroup/InterestGroup";
import NavBar from "../../Components/NavBar/NavBar";
import { setUserInterests } from "../../api/setAPI";
import { useNavigate } from "react-router-dom";

const ChooseYourInterestsPage = () => {
  const navigate = useNavigate();

  const [selectedInterests, setSelectedInterests] = useState([]);
  const [statusMessage, setStatusMessage] = useState(null);

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
    try {
      const response = await setUserInterests(selectedInterests);
      setStatusMessage(response.message);
      setTimeout(() => {
        navigate("/for-you", { replace: "true" });
      }, 1000);
    } catch (err) {
      setStatusMessage(err.message);
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

        <div>
          <button className="submit-button" onClick={handleSubmit}>
            Confirm
          </button>
        </div>
        {statusMessage && <p className="status-message">{statusMessage}</p>}
      </div>
    </>
  );
};

export default ChooseYourInterestsPage;
