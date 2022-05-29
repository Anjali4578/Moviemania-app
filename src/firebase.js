import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyBX00hl4Xqju_lBa94QMNouetuuZlCMMK8",
  authDomain: "moviemania-web.firebaseapp.com",
  projectId: "moviemania-web",
  storageBucket: "moviemania-web.appspot.com",
  messagingSenderId: "49597269986",
  appId: "1:49597269986:web:e576e41b6b40f02fe55bbb",
  measurementId: "G-WC3NZD8HF0",
};

const firebaseApp = initializeApp(firebaseConfig);
const db = getFirestore(firebaseApp);
export const auth = getAuth(firebaseApp);

export default db;
