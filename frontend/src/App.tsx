import { useEffect, useState } from "react";
import HomePage from "./HomePage";
import { LanguageProvider } from "./LanguageProvider";
import { jwtDecode, JwtPayload } from "jwt-decode";

const cognitoAuthURL = import.meta.env.VITE_COGNITO_AUTH_URL;
const cognitoClientID = import.meta.env.VITE_COGNITO_CLIENT_ID;
const cognitoRedirectURL = import.meta.env.VITE_COGNITO_REDIRECT_URL;
const cognitoLogoutRedirectURL = import.meta.env
  .VITE_COGNITO_POST_LOGOUT_REDIRECT_URL;

interface CustomJwtPayload extends JwtPayload {
  name?: string;
}

const handleAuthCallback = () => {
  const hash = window.location.hash;
  const params = new URLSearchParams(hash.slice(1));
  const idToken = params.get("id_token");
  if (idToken) {
    localStorage.setItem("id_token", idToken);
  }
  const accessToken = params.get("access_token");
  if (accessToken) {
    localStorage.setItem("access_token", accessToken);
  }
  console.log("id_token", idToken, "access_token", accessToken);
  window.location.href = "/"; // Redirect to home
};

const login = () => {
  const cognitoUrl = `${cognitoAuthURL}/login?response_type=token&client_id=${cognitoClientID}&redirect_uri=${cognitoRedirectURL}/callback`;
  window.location.href = cognitoUrl;
};

const App = () => {
  const token = localStorage.getItem("id_token");
  const [user, setUser] = useState<CustomJwtPayload | undefined>(undefined);

  useEffect(() => {
    const currentPath = window.location.pathname;
    if (currentPath === "/callback") {
      handleAuthCallback();
    }
  }, []);

  useEffect(() => {
    if (token) {
      const decodedToken = jwtDecode(token);
      console.log(decodedToken);
      setUser(decodedToken);
    }
  }, [token]);

  if (!token) {
    return <button onClick={login}>Login</button>;
  }

  const signOut = () => {
    localStorage.removeItem("id_token");

    const cognitoURL = `${cognitoAuthURL}/logout?client_id=${cognitoClientID}&logout_uri=${cognitoLogoutRedirectURL}`;
    window.location.href = cognitoURL;
  };
  const unknown = "unknown user 👽";
  const username = user ? { name: user.name || unknown } : { name: unknown };
  return (
    // <Authenticator>
    //   {({ signOut, user }) => (
    //     <>
    <LanguageProvider>
      <HomePage signOut={signOut} user={username} />
    </LanguageProvider>
    //     </>
    //   )}
    // </Authenticator>
  );
};

export default App;
