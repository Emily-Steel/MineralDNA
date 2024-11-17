import React, { useState } from "react";
import LanguageToggle from "./LanguageToggle";
import MineralDNAReport from "./MineralDNAReport";

const apiURL = import.meta.env.VITE_API_URL;

interface DNAResponse {
  origin: string;
  elevation: string;
  present: string;
  daily_life_decision: string;
  identity: string;
  interaction: string;
  communication: string;
  immediate_decision: string;
  soul: string;
  truth: string;
  guidance: string;
  repeat_decisions: string;
  experimentation: string;
}

const dnaResponseToArray = (r: DNAResponse) => {
  const fields: string[] = [];
  Object.entries(r).forEach(([_, v]) => {
    const value =
      typeof v === "object" && v !== null ? JSON.stringify(v) : String(v);
    fields.push(value);
  });
  return fields;
};

const MineralDNAForm: React.FC = () => {
  const [names, setNames] = useState("");
  const [surnames, setSurnames] = useState("");
  const [dob, setDob] = useState("");
  const [submittedNames, setSubmittedNames] = useState("");
  const [submittedSurnames, setSubmittedSurnames] = useState("");
  const [submittedDOB, setSubmittedDOB] = useState("");
  const [results, setResults] = useState<DNAResponse | undefined>();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const formattedDOB = dob.replace(/-/g, "/");

    const payload = {
      names: names,
      surnames: surnames,
      dob: formattedDOB,
    };

    setSubmittedNames(names);
    setSubmittedSurnames(surnames);
    setSubmittedDOB(formattedDOB);

    try {
      const response = await fetch(`${apiURL}/mineral_dna`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(
          `HTTP error! Status: ${response.status}, Body: ${response.body}`
        );
      }

      const data = await response.json();
      const stones = data["stones"];
      setResults(stones);
    } catch (error) {
      console.error("Error fetching results:", error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Get your mineral DNA:</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Names:
            <input
              type="text"
              value={names}
              onChange={(e) => setNames(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Surnames:
            <input
              type="text"
              value={surnames}
              onChange={(e) => setSurnames(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Date of Birth:
            <input
              type="date"
              value={dob}
              onChange={(e) => setDob(e.target.value)}
              required
            />
          </label>
        </div>
        <button type="submit">Submit</button>
      </form>
      {results !== undefined && (
        <article>
          <h2>DNA report</h2>
          <LanguageToggle />
          <MineralDNAReport
            names={submittedNames}
            surnames={submittedSurnames}
            dob={submittedDOB}
            dna={dnaResponseToArray(results)}
          />
        </article>
      )}
    </div>
  );
};

export default MineralDNAForm;
export type { DNAResponse };
