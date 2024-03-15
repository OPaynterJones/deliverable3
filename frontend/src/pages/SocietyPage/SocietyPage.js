import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";

function SocietyPage() {
  const { societyName } = useParams();

  const [societyDetails, setSocietyDetails] = useState(null);
  //   useEffect(() => {
  //     const fetchSocietyDetails = async () => {
  //       const response = await fetch(`/api/societies/${societyName}`); // Adjust API endpoint
  //       const data = await response.json();
  //       setSocietyDetails(data);
  //     };
  //     fetchSocietyDetails();
  //   }, [societyName]);

  return (
    <div>
      {societyDetails ? (
        <>
          <h1>{societyDetails.name}</h1>
          <p>{societyDetails.description}</p>
        </>
      ) : (
        <p>Loading society details for {societyName}</p>
      )}
    </div>
  );
}

export default SocietyPage;
