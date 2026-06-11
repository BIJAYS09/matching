"use client"

import {

    Badge

} from "@/components/ui/badge"


type Props = {

    skills: string[]

    selectedSkills: string[]

    setSelectedSkills: (
        skills: string[]
    ) => void
}


export default function SkillFilters({

    skills,

    selectedSkills,

    setSelectedSkills

}: Props) {

    function toggleSkill(skill: string) {

        if (
            selectedSkills.includes(skill)
        ) {

            setSelectedSkills(

                selectedSkills.filter(
                    (s) => s !== skill
                )
            )

        } else {

            setSelectedSkills([
                ...selectedSkills,
                skill
            ])
        }
    }

    return (

        <div className="flex flex-wrap gap-2">

            {skills.map((skill) => {

                const active = selectedSkills.includes(
                    skill
                )

                return (

                    <Badge

                        key={skill}

                        variant={
                            active
                                ? "default"
                                : "outline"
                        }

                        className="cursor-pointer px-3 py-1 text-sm"

                        onClick={() =>
                            toggleSkill(skill)
                        }
                    >

                        {skill}

                    </Badge>
                )
            })}
        </div>
    )
}