import http from "k6/http";
import { check, sleep } from "k6";

// Test configuration
export const options = {
  thresholds: {
    // Assert that 99% of requests finish within 3000ms.
    http_req_duration: ["p(99) < 3000"],
  },
  // Ramp the number of virtual users up and down
  stages: [
    { duration: "3s", target: 20 },
    { duration: "7s", target: 150 },
    { duration: "3s", target: 50 },
  ],
};

// Simulated user behavior
export default function () {
  let res = http.get("http://project.local");
  // Validate response status
  check(res, { "status was 200": (r) => r.status == 200 });
  sleep(1);
}
