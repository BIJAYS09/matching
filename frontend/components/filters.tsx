"use client"

import {

    Input

} from "@/components/ui/input"

import {

    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue

} from "@/components/ui/select"


type Props = {

    search: string

    setSearch: (v: string) => void

    minScore: string

    setMinScore: (v: string) => void
}


export default function Filters({

    search,

    setSearch,

    minScore,

    setMinScore

}: Props) {

    return (

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">

            <Input

                placeholder="Search jobs, skills, companies..."

                value={search}

                onChange={(e) =>

                    setSearch(e.target.value)
                }
            />

            <Select

                value={minScore}

                onValueChange={setMinScore}
            >

                <SelectTrigger>

                    <SelectValue placeholder="Minimum Score" />

                </SelectTrigger>

                <SelectContent>

                    <SelectItem value="0">
                        Any Score
                    </SelectItem>

                    <SelectItem value="0.5">
                        50%+
                    </SelectItem>

                    <SelectItem value="0.6">
                        60%+
                    </SelectItem>

                    <SelectItem value="0.7">
                        70%+
                    </SelectItem>

                    <SelectItem value="0.8">
                        80%+
                    </SelectItem>

                </SelectContent>

            </Select>

        </div>
    )
}