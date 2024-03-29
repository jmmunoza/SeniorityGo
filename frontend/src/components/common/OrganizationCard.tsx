import { Organization } from '../../models/Organization';
import { useTranslation } from 'react-i18next';


interface OrganizationCardProps {
    organization: Organization;
}

function OrganizationCard({ organization }: OrganizationCardProps) {
    const { t } = useTranslation();

    return (
        <div className="h-full transition ease-in-out hover:bg-indigo-500 duration-150 rounded-2xl bg-gradient-to-r from-fuchsia-700 to-blue-600 p-1 shadow-2xl">
            <div className="h-full transition block rounded-xl hover:bg-gray-800/50 duration-150 bg-gray-800/80 p-4 sm:p-6 lg:p-8">
                <div className="text-center space-y-8">

                    <div className="flex items-center gap-4">
                        <img className="h-20 lg:h-24 py-4  object-cover" src={organization.getImage()} alt="avatar" />
                        <h3 className="text-xl lg:text-3xl font-medium text-white">{organization.getName()}</h3>
                    </div>
                   
                    <hr className="h-px  bg-gradient-to-r from-fuchsia-700 to-blue-600 border-0" />

                    <div className="w-full">
                        <dl className="grid max-w-screen-xl grid-cols-1 gap-8 mx-auto sm:grid-cols-3 text-white">
                            <div className="flex flex-col items-center justify-center">
                                <dt className="mb-2 text-6xl font-extrabold">{organization.getProfiles().length}</dt>
                                <dd className="text-gray-400">{t('profiles')}</dd>
                            </div>
                            <div className="flex flex-col items-center justify-center">
                                <dt className="mb-2 text-6xl font-extrabold">{organization.getRequirements().length}</dt>
                                <dd className="text-gray-400">{t('requirements')}</dd>
                            </div>
                            <div className="flex flex-col items-center justify-center">
                                <dt className="mb-2 text-6xl font-extrabold">{organization.getSeniorities().length}</dt>
                                <dd className="text-gray-400">{t('seniorities')}</dd>
                            </div>
                        </dl>
                    </div>

                    <hr className="h-px bg-gradient-to-r from-fuchsia-700 to-blue-600 border-0" />

                    <h3 className="text-lg  font-bold text-gray-200 sm:text-xl">
                        {t('seniorities')}
                    </h3>

                    <ul className="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-2">
                        {organization.getSeniorities().map((seniority) => {
                            return (
                                <li>
                                    <div className="block h-full text-base rounded-lg border-2 border-blue-600 px-4 py-1.5 hover:border-fuchsia-700">
                                        <strong className="font-medium text-sm text-white">{seniority.getName()}</strong>
                                    </div>
                                </li>
                            )
                        })}
                    </ul>

                    <hr className="h-px bg-gradient-to-r from-fuchsia-700 to-blue-600 border-0" />

                    <h3 className="text-lg  font-bold text-gray-200 sm:text-xl">
                        {t('profiles')}
                    </h3>

                    <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                        {organization.getProfiles().map((profile) => {
                            return (
                                <li>
                                    <div className="block h-full text-base rounded-lg border-2 border-blue-600 px-4 py-1.5 hover:border-fuchsia-700">
                                        <strong className="font-medium text-sm text-white">{profile.getName()}</strong>
                                    </div>
                                </li>
                            )
                        })}
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default OrganizationCard;