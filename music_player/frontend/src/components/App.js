import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import HomePage from "./HomePage";

/**
 * @returns {JSX.Element} The root application component
 */
function App() {
  return (
    <StrictMode>
      <div>
        <HomePage />
      </div>
    </StrictMode>
  );
}

const container = document.getElementById("app");
if (!container) throw new Error("Failed to find the root element");
const root = createRoot(container);
root.render(<App />);

export default App;
