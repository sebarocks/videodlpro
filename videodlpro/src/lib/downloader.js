import io from "socket.io-client";

const ADDR = "localhost:8000";
const socket = io(`ws://${ADDR}`, { path: "/ws/" });

export default socket;

