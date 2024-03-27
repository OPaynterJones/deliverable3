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
    console.log(await response.json());
    throw new Error("Failed to update information");
  }
};

export const setUserInterests = async (interests) => {
  const response = await fetch("http://localhost:5000/add_interests", {
    method: "POST",
    credentials: "include",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({ interests }),
  });
  if (!response.ok) {
    const resp = await response.json();
    throw new Error(resp.message);
  }

  const data = await response.json();
  return data;
};
