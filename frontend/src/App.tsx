//import { Authenticator } from "@aws-amplify/ui-react";
import HomePage from "./HomePage";
import { LanguageProvider } from "./LanguageProvider";

function App() {
  const signOut = () => {};
  const user = { username: "emilysteel" };
  return (
    // <Authenticator>
    //   {({ signOut, user }) => (
    //     <>
    <LanguageProvider>
      <HomePage signOut={signOut} user={user} />
    </LanguageProvider>
    //     </>
    //   )}
    // </Authenticator>
  );
}

export default App;
