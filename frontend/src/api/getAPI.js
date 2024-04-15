export const fetchSocieties = async () => {
  const response = await fetch(`http://${window.location.hostname}:5000/societies`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch societies");
  }

  const data = await response.json();
  return data.society_names;
};

export const getSociety = async (society_name) => {
  const response = await fetch(
    `http://${window.location.hostname}:5000/societies/${society_name}`
  );
  const data = await response.json();
  return data;
};
