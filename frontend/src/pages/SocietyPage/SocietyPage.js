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
  const [editableDetails, setEditableDetails] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const societyDetails = await getSociety(society_name);
      setSocietyDetails(societyDetails);

      if (societyDetails && societyDetails.society_id) {
        const response = await checkSession(societyDetails.society_id);
        setEditPermissions(response.hasEditPermissions);
      }
    };

    fetchData();
  }, [society_name]);

  useEffect(() => {
    if (isEditing || !societyDetails) return;

    updateInformation("http://localhost:5000/societies", societyDetails);
  }, [isEditing]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setSocietyDetails((prevDetails) => ({
      ...prevDetails,
      [name]: value,
    }));
  };

  useEffect(() => {
    console.log(societyDetails);
  }, [societyDetails]);

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
          <div className="society-container">
            <div className="society-name">
              <h1>{societyDetails.name}</h1>
              <hr />
            </div>
            <div className="society-info-container">
              {isEditing ? (
                <div>
                  <textarea
                    className="description"
                    name="description"
                    value={societyDetails.description}
                    onChange={handleInputChange}
                  />
                </div>
              ) : (
                <p className="description">{societyDetails.description}</p>
              )}
              <table className="details-table">
                <tbody>
                  {Object.entries(societyDetails)
                    .filter(([key]) => !blacklist.includes(key))
                    .map(([key, value]) => (
                      <tr className="society-detail" key={key}>
                        <td className="society-detail-key">
                          {key.charAt(0).toUpperCase() + key.slice(1)}:
                        </td>
                        <td className="society-detail-value" >
                          {isEditing ? (
                            <textarea
                              type="text"
                              name={key}
                              value={societyDetails[key]}
                              onChange={handleInputChange}
                            />
                          ) : (
                            value
                          )}
                        </td>
                      </tr>
                    ))}
                </tbody>
              </table>
              {hasEditPermissions && (
                <div>
                  {isEditing ? ( // Render save button if editing is enabled
                    <button
                      className="edit-button"
                      onClick={() => setIsEditing(!isEditing)}
                    >
                      Save
                    </button>
                  ) : (
                    // Render edit button if editing is not enabled
                    <button
                      className="edit-button"
                      onClick={() => setIsEditing(!isEditing)}
                    >
                      Edit Society
                    </button>
                  )}
                </div>
              )}
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
