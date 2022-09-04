import io from "socket.io-client";
import { env } from '$env/dynamic/public';

console.log(env.PUBLIC_HOSTNAME);
const socket = io(`${env.PUBLIC_HOSTNAME}`, { path: "/api/ws/" });

export default socket;

