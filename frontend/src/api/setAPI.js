export const updateInformation = async (url, data) => {
  const response = await fetch(url, {
    method: "PUT",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ data }),
  });

  if (!response.ok) {
    console.log(await response.json())
    throw new Error("Failed to update information");
  }
};
