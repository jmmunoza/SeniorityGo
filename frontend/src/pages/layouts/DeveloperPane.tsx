import { Outlet } from "react-router-dom";
import AppBackround from '../../assests/images/AppBackground.jpg';
import DeveloperHeader from "../../components/developer/DeveloperHeader";
import DeveloperFooter from "../../components/developer/DeveloperFooter";

function DeveloperPaneLayout() {

    return (
        <div className="w-full h-screen bg-center bg-cover" style={{ backgroundImage: `url(${AppBackround})` }}>
            <div className="w-full h-screen flex flex-col bg-gradient-to-r from-gray-900/95  to-dark-blue-900/95">
                <header className="z-10">
                    <DeveloperHeader />
                </header>
                <main className="w-full h-full flex overflow-hidden mx-auto">
                    <Outlet />
                </main>
                <footer className="z-10">
                    <DeveloperFooter />
                </footer>
            </div>
        </div>

    );
}

export default DeveloperPaneLayout;