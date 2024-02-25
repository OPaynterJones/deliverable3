import React from "react";
import "./InputField.css";

const InputField = ({ type, fieldToAskFor, value, onChange }) => (
  <div className="inputFieldContainer">
    <input
      type={type}
      name={fieldToAskFor}
      placeholder=""
      autoCorrect="off"
      required
      value={value}
      onChange={onChange}
    />
    <div className="inputFieldLabel"> {fieldToAskFor} </div>
  </div>
);

export default InputField;
