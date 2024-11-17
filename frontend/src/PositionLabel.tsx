import React from "react";
import { useLanguage } from "./LanguageProvider";

import positionTableData from "./data/positions.json";

interface PositionProps {
  positionID: string;
}

const positionTable: Record<string, { en: string; fr: string }> =
  positionTableData;

const PositionLabel: React.FC<PositionProps> = ({
  positionID: positionNumber,
}) => {
  const { language } = useLanguage();
  const position = positionTable[positionNumber];

  if (!position) {
    return <div>Position not found</div>;
  }

  const name = position[language];
  let label = name;
  if (language == "en") {
    label = `${name} stone`;
  }
  if (language == "fr") {
    label = `La pierre ${name.toLowerCase()}`;
  }

  return <strong>{label}: </strong>;
};

export default PositionLabel;
