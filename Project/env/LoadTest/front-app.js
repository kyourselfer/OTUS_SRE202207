import http from 'k6/http';
import { sleep } from 'k6';


// export let options = {
//   insecureSkipTLSVerify: false,
//   noConnectionReuse: false,
//   vus: 250,
//   duration: '30s'
// };

export let options = {
  insecureSkipTLSVerify: false,
  noConnectionReuse: false,
  stages: [
    {duration: '1m', target: 500},
    {duration: '5m', target: 500},
    {duration: '1m', target: 0},
  ]
};

// export let options = {
//   insecureSkipTLSVerify: false,
//   noConnectionReuse: true,
//   stages: [
//     {duration: '10s', target: 100},
//     {duration: '1m', target: 100},
//     {duration: '10s', target: 1400},
//     {duration: '3m', target: 1400},
//     {duration: '10s', target: 100},
//     {duration: '3m', target: 100},
//     {duration: '10s', target: 0},
//   ]
// };

export default (data) => {
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  getAllCategory(params);
  getAttachments(params);

  //sleep(1);
};
