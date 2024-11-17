import worlds from "./data/dna.json";
import { useLanguage } from "./LanguageProvider";
import Mineral from "./MineralItem";
import PositionLabel from "./PositionLabel";

interface MineralDNAReportProps {
  names: string;
  surnames: string;
  dob: string;
  dna: Array<string>;
}

const MineralDNAReport: React.FC<MineralDNAReportProps> = ({
  names,
  surnames,
  dob,
  dna,
}: MineralDNAReportProps) => {
  const { language } = useLanguage();

  const renderPosition = (posID: number) => {
    return (
      <>
        <li key={"position-" + posID}>
          <PositionLabel positionID={posID.toString()} />
          <Mineral mineralID={dna[posID - 1]} />
        </li>
      </>
    );
  };

  return (
    <div>
      <h2>
        {names} {surnames}
      </h2>
      {language == "en" && <h3>Born {dob}</h3>}
      {language == "fr" && <h3>Né∙e le {dob}</h3>}
      <section>
        <p className="section-label">{worlds["MATERIAL"][language]}</p>
        <ul>{[1, 2, 3].map((i) => renderPosition(i))}</ul>
        <div className="section-footer">{renderPosition(4)}</div>
      </section>
      <section>
        <p className="section-label">{worlds["MENTAL"][language]}</p>
        <ul>{[5, 6, 7].map((i) => renderPosition(i))}</ul>
        <div className="section-footer">{renderPosition(8)}</div>
      </section>
      <section>
        <p className="section-label">{worlds["SPIRITUAL"][language]}</p>
        <ul>{[9, 10, 11].map((i) => renderPosition(i))}</ul>
        <div className="section-footer">{renderPosition(12)}</div>
      </section>
      {renderPosition(13)}
    </div>
  );
};

export default MineralDNAReport;
