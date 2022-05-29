import React from "react";
import "./PlansScreen.css";

function PlansScreen() {
  return (
    <div className="plansScreen__plan">
      <div className="plansScreen__info">
        <div className="details">
          <div className="line">
            <p>
              <h5>Premium</h5>
              <h6>4K + HDR</h6>
            </p>
            <button>Subscribe</button>
          </div>
          <div className="line">
            <p>
              <h5>Standard</h5>
              <h6>1080p</h6>
            </p>
            <button>Subscribe</button>
          </div>
          <div className="line">
            <p>
              <h5>Basic</h5>
              <h6>720p</h6>
            </p>
            <button>Subscribe</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PlansScreen;
