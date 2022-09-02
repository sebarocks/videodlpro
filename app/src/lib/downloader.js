import io from "socket.io-client";
import { env } from '$env/dynamic/public';

console.log(`ws://${env.PUBLIC_API_URL}`);
const socket = io(`ws://${env.PUBLIC_HOSTNAME}`, { path: "/api/ws/" });

export default socket;

