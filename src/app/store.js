import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../features/userSlice";

export const store = configureStore({
  reducer: {
    user: userReducer,
  },
});

/* export default configureStore({
  reducer: {
    user: userReducer,
  },
}) */