import React from "react";
import MineralDNAForm from "./MineralDNAForm";
//import Auth from "aws-amplify";

interface HomePageProps {
  signOut: () => void;
  user: { name: string };
}

const HomePage: React.FC<HomePageProps> = ({ signOut, user }) => {
  return (
    <div>
      <h1>Welcome, {user.name}!</h1>
      <MineralDNAForm />
      <button onClick={signOut}>Sign out</button>
    </div>
  );
};

export default HomePage;
