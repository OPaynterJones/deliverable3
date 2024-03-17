import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import "./SocietyPage.css";

function SocietyPage() {
  const { society_name } = useParams();

  const [societyDetails, setSocietyDetails] = useState(null);

  useEffect(() => {
    const fetchSocietyDetails = async () => {
      const response = await fetch(
        `http://localhost:5000/societies/${society_name}`
      );
      const data = await response.json();
      setSocietyDetails(data);
    };
    fetchSocietyDetails();
  }, [society_name]);

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
              <p className="description">{societyDetails.description}</p>
              <tbody>
                {Object.entries(societyDetails).map(([key, value]) => (
                  <tr className="society-detail" key={key}>
                    <td className="society-detail-key">
                      {key.charAt(0).toUpperCase() + key.slice(1)}:
                    </td>
                    <td className="society-detail-value">{value}</td>
                  </tr>
                ))}
              </tbody>
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
