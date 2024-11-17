import React from "react";
import { useLanguage } from "./LanguageProvider";

const LanguageToggle: React.FC = () => {
  const { language, setLanguage } = useLanguage();

  const toggleLanguage = () => {
    setLanguage(language === "en" ? "fr" : "en");
  };

  return (
    <button onClick={toggleLanguage}>
      Switch to {language === "en" ? "French" : "English"}
    </button>
  );
};

export default LanguageToggle;
