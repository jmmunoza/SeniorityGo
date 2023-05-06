import { Navigate, Route } from 'react-router-dom';
import DeveloperPageLayout from '../pages/layouts/DeveloperPane';
import SelectProfilePage from '../pages/developer/SelectProfilePage';
import { ReactElement } from 'react';


const ProtectedRoute = ({ children }: { children: ReactElement }) => {
    if (localStorage.getItem('access_token') === null) {
        return <Navigate to="/login" replace />;
    }

    return children;
};


const DeveloperRoutes = [
    <Route path='/' element={
        <ProtectedRoute>
            <DeveloperPageLayout />
        </ProtectedRoute>
    }>
        <Route path='/profiles' element={<SelectProfilePage />} />
    </Route>
];

export default DeveloperRoutes;