import { useTranslation } from 'react-i18next';
import { Developer } from '../../models/Developer';
import DeveloperRequirementCard from './DeveloperRequirementCard';


interface UserRequirementsCardProps {
    user: Developer | null;
}


function UserRequirementsCard({ user }: UserRequirementsCardProps) {
    // Translation component
    const { t } = useTranslation();

    return (
        <div className='w-full sm:w-2/3 p-4'>
            <div className='rounded-lg p-4 lg:p-8 bg-gradient-to-r from-gray-800 to-dark-blue-800 shadow-2xl space-y-4 lg:space-y-8'>
                <h3 className="text-3xl font-extrabold text-white">{t('requirements')}</h3>
                <div className='grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-2'>
                    {user?.getDeveloperRequirements().map((developerrequirement) => (<DeveloperRequirementCard developerrequirement={developerrequirement} />))}
                </div>
            </div>
        </div>
    );
}

export default UserRequirementsCard;