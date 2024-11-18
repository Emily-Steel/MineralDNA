import React from "react";
import { useLanguage } from "./LanguageProvider";

import mineralTableData from "./data/minerals.json";

interface MineralProps {
  mineralID: string;
}

const mineralTable: Record<string, { en: string; fr: string; image: string }> =
  mineralTableData;

const Mineral: React.FC<MineralProps> = ({ mineralID: mineralNumber }) => {
  const { language } = useLanguage();
  const mineral = mineralTable[mineralNumber];

  if (!mineral) {
    return <div>Mineral not found</div>;
  }

  return (
    <>
      <span style={{ height: "50px", lineHeight: "50px" }}>
        {mineral[language]}{" "}
      </span>
      {/* <img
        src={mineral.image}
        alt={mineral[language]}
        style={{ width: "50px" }}
      /> */}
    </>
  );
};

export default Mineral;
