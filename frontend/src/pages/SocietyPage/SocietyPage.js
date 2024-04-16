import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import "./SocietyPage.css";
import { getSociety } from "../../api/getAPI";
import { checkSession } from "../../api/authAPI";
import { updateInformation } from "../../api/setAPI";

function SocietyPage() {
  const { society_name } = useParams();
  const [societyDetails, setSocietyDetails] = useState(null);

  const [hasEditPermissions, setEditPermissions] = useState(false);

  const [isEditing, setIsEditing] = useState(false);


  useEffect(() => {
    const fetchData = async () => {
      const societyDetails = await getSociety(society_name);
      setSocietyDetails(societyDetails);
      try {
        if (societyDetails && societyDetails.society_id) {
          const response = await checkSession(societyDetails.society_id);
          setEditPermissions(response.hasEditPermissions);
        }
      } catch {}
    };

    fetchData();
  }, [society_name]);

  useEffect(() => {
    if (isEditing || !societyDetails) return;

    const updatedSocietyDetails = { ...societyDetails };
    const editableDivs = document.querySelectorAll(
      ".society-info-container div[contenteditable]"
    );

    for (const editableDiv of editableDivs) {
      const key = editableDiv.getAttribute("name");
      updatedSocietyDetails[key] = editableDiv.textContent.trim();
    }

    updateInformation(`http://${window.location.hostname}:5000/societies`, updatedSocietyDetails);
    setSocietyDetails(updatedSocietyDetails);
  }, [isEditing]);

  const blacklist = ["description", "society_id", "name", "image_url"];

  return (
    <div className="society-page">
      {societyDetails ? (
        <>
          {societyDetails.image_url && (
            <img
              className="society-image"
              src={societyDetails.image_url}
              alt={societyDetails.name}
            />
          )}
          {hasEditPermissions && (
            <div className="button-container">
              <button
                className="edit-button"
                onClick={() => setIsEditing(!isEditing)}
              >
                {isEditing ? "Save" : "Edit"}
              </button>
            </div>
          )}
          <div className="society-container">
            <div className="society-name">
              <h1>{societyDetails.name}</h1>
              <hr />
            </div>
            <div className="society-info-container">
              <div
                className="description"
                contentEditable={isEditing ? "true" : "false"}
                name="description"
                style={
                  isEditing ? { border: "2px solid var(--primary-color)" } : {}
                }
                suppressContentEditableWarning="true"
              >
                {societyDetails.description}
              </div>
              <div className="extra-info-container">
                {Object.entries(societyDetails)
                  .filter(([key]) => !blacklist.includes(key))
                  .map(([key, value]) => (
                    <div className="society-detail" key={key}>
                      <div className="society-detail-key">
                        {key.charAt(0).toUpperCase() + key.slice(1)}:
                      </div>
                      <div
                        className="society-detail-value"
                        contentEditable={isEditing ? "true" : "false"}
                        name={key}
                        style={
                          isEditing
                            ? { border: "2px solid var(--primary-color)" }
                            : {}
                        }
                        suppressContentEditableWarning="true"
                      >
                        {societyDetails[key]}
                      </div>
                    </div>
                  ))}
              </div>
            </div>
          </div>
        </>
      ) : (
        <p>Loading society details for {society_name}</p>
      )}
    </div>
  );
}

export default SocietyPage;
