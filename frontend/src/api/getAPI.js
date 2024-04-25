import { backendUrl } from "../config";

export const fetchSocieties = async () => {
  const response = await fetch(`${backendUrl}/societies`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch societies");
  }

  const data = await response.json();
  return data.society_names;
};

export const getSociety = async (society_name) => {
  const response = await fetch(`${backendUrl}/${society_name}`);
  const data = await response.json();
  return data;
};
