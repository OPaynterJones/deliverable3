export const checkSession = async (society_id = null) => {
  const response = await fetch("http://localhost:5000/check_session", {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ society_id }),
  });

  if (!response.ok) {
    if (response.status === 401) {
      return { sessionValid: false };
    }
    const errorData = await response.json();
    throw new Error(errorData.message);
  }

  const data = await response.json();
  return { sessionValid: true, hasEditPermissions: data.has_edit_permissions };
};

export const checkHasInterests = async () => {
  const response = await fetch("http://localhost:5000/has_interests", {
    method: "POST",
    credentials: "include",
  });

  if (!response.ok) {
    return false;
  }

  return true;
};
