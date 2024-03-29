import './App.css';
import { Routes } from 'react-router-dom';
import AdminRoutes from './routes/AdminRoutes';
import DeveloperRoutes from './routes/DeveloperRoutes';
import WithioutCredentialsRoutes from './routes/WithoutCredentialsRoutes';
import FreeAccessRoutes from './routes/FreeAccessRoutes';
import LoggedRoutes from './routes/LoggedRoutes';
import NotificationBar from './components/common/NotificationsBar';

function App() {
	return (
		<div>
			<Routes>
				{FreeAccessRoutes},
				{AdminRoutes},
				{DeveloperRoutes},
				{WithioutCredentialsRoutes},
				{LoggedRoutes}
			</Routes>
			<NotificationBar />
		</div>
	);
}

export default App;
