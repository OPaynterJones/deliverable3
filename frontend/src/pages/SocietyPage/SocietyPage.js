import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import "./SocietyPage.css";
import { getSociety } from "../../api/getAPI";
import { checkSession } from "../../api/authAPI";

function SocietyPage() {
  const [hasEditPermissions, setEditPermissions] = useState(false);
  const [isEditing, setIsEditing] = useState(false); // State to track whether editing is enabled
  const { society_name } = useParams();

  const [societyDetails, setSocietyDetails] = useState(null);
  const [editableDetails, setEditableDetails] = useState({}); // State to store editable details

  useEffect(() => {
    getSociety(society_name).then(setSocietyDetails);
  }, [society_name]);

  useEffect(() => {
    const checkLoggedIn = async () => {
      if (societyDetails && societyDetails.society_id) {
        const response = await checkSession(societyDetails.society_id);
        setEditPermissions(response.hasEditPermissions);
      }
    };

    checkLoggedIn();
  }, [societyDetails]);

  useEffect(() => {
    if (isEditing && societyDetails) {
      setEditableDetails({ ...societyDetails });
    }
  }, [isEditing, societyDetails]);

  const handleEditClick = () => {
    setIsEditing(true);
  };

  const handleSaveClick = () => {
    setIsEditing(false);
    setSocietyDetails(editableDetails);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEditableDetails((prevDetails) => ({
      ...prevDetails,
      [name]: value,
    }));
  };

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
                    name="description"
                    value={editableDetails.description}
                    onChange={handleInputChange}
                  />
                </div>
              ) : (
                <p className="description">{societyDetails.description}</p>
              )}
              <table>
                <tbody>
                  {Object.entries(societyDetails).map(([key, value]) => (
                    <tr className="society-detail" key={key}>
                      <td className="society-detail-key">
                        {key.charAt(0).toUpperCase() + key.slice(1)}:
                      </td>
                      <td className="society-detail-value">
                        {isEditing ? (
                          <input
                            type="text"
                            name={key}
                            value={editableDetails[key]}
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
                    <button className="edit-button" onClick={handleSaveClick}>
                      Save
                    </button>
                  ) : ( // Render edit button if editing is not enabled
                    <button className="edit-button" onClick={handleEditClick}>
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
