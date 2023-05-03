import { ProfileSeniority } from './ProfileSeniority';
import { Requirement } from './Requirement';

export class ProfileSeniorityRequirement {
    private _profileseniority: ProfileSeniority;
    private _requirement: Requirement;

    constructor(profileseniority: ProfileSeniority, requirement: Requirement) {
        this._profileseniority = profileseniority;
        this._requirement = requirement;
    }

    public getProfileSeniority(): ProfileSeniority {
        return this._profileseniority;
    }

    public setProfileSeniority(profileseniority: ProfileSeniority): void {
        this._profileseniority = profileseniority;
    }

    public getRequirement(): Requirement {
        return this._requirement;
    }

    public setRequirement(requirement: Requirement): void {
        this._requirement = requirement;
    }
}
