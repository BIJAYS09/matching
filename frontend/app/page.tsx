"use client"

import {

    useEffect,
    useState

} from "react"

import api from "@/lib/api"

import UploadCV from "@/components/upload-cv"

import {

    Card,
    CardContent

} from "@/components/ui/card"

import {

    Button

} from "@/components/ui/button"

import {

    Badge

} from "@/components/ui/badge"

import {

    Input

} from "@/components/ui/input"

export default function HomePage() {

    const [cvs, setCVs] = useState<any[]>([])

    const [jobs, setJobs] = useState<any[]>([])

    const [matches, setMatches] = useState<any[]>([])

    const [selectedCV, setSelectedCV] = useState<any>(null)

    const [jobUrl, setJobUrl] = useState("")

    const [loadingJob, setLoadingJob] = useState(false)

    useEffect(() => {

        fetchCVs()

        fetchJobs()

    }, [])


    async function addJob() {

    if (!jobUrl) return

    setLoadingJob(true)

    try {

        await api.post(

            "/add-job",

            null,

            {
                params: {
                    url: jobUrl
                }
            }
        )

        setJobUrl("")

        fetchJobs()

    } catch (err) {

        console.error(err)

    } finally {

        setLoadingJob(false)
    }
}

    async function fetchCVs() {

        const response = await api.get(
            "/cvs"
        )

        setCVs(response.data)
    }


    async function fetchJobs() {

        const response = await api.get(
            "/jobs"
        )

        setJobs(response.data)
    }


    async function findMatches(cvId: number) {

        const response = await api.get(
            `/matches/${cvId}`
        )

        setMatches(response.data)

        setSelectedCV(cvId)
    }


    return (

        <main className="min-h-screen bg-muted/40">

            <div className="grid grid-cols-12 gap-6 p-6">

                {/* ---------------- */}
                {/* LEFT SIDEBAR */}
                {/* ---------------- */}

                <div className="col-span-3 space-y-4">

                    <UploadCV
                        onUploadSuccess={() => {

                            fetchCVs()
                        }}
                    />

                    <Card>

                        <CardContent className="p-4 space-y-4">

                            <h2 className="text-xl font-semibold">

                                Candidates

                            </h2>

                            <div className="space-y-3">

                                {cvs.map((cv) => (

                                    <div

                                        key={cv.id}

                                        className="border rounded-lg p-3 space-y-2"

                                    >

                                        <div>

                                            <p className="font-medium">

                                                {cv.name}

                                            </p>

                                            <p className="text-sm text-muted-foreground">

                                                {cv.email}

                                            </p>

                                        </div>

                                        <Button

                                            className="w-full"

                                            onClick={() =>

                                                findMatches(cv.id)
                                            }
                                        >

                                            Find Matches

                                        </Button>

                                    </div>
                                ))}
                            </div>

                        </CardContent>

                    </Card>

                </div>

                {/* ---------------- */}
                {/* RIGHT CONTENT */}
                {/* ---------------- */}

                <div className="col-span-9 space-y-6">
                    {/* ---------------- */}
{/* ADD JOB */}
{/* ---------------- */}

<Card>

    <CardContent className="p-6 space-y-4">

        <div className="space-y-1">

            <h2 className="text-2xl font-semibold">

                Add Job URL

            </h2>

            <p className="text-muted-foreground">

                Paste a company job URL
                to extract structured
                job information.

            </p>

        </div>

        <div className="flex gap-3">

            <Input

                placeholder="https://company.com/job"

                value={jobUrl}

                onChange={(e) =>

                    setJobUrl(
                        e.target.value
                    )
                }
            />

            <Button

                onClick={addJob}

                disabled={loadingJob}
            >

                {loadingJob
                    ? "Extracting..."
                    : "Add Job"}

            </Button>

        </div>

    </CardContent>

</Card>
                    {/* ---------------- */}
                    {/* JOBS */}
                    {/* ---------------- */}

                    <Card>

                        <CardContent className="p-6 space-y-4">

                            <h2 className="text-2xl font-semibold">

                                Available Jobs

                            </h2>

                            <div className="grid grid-cols-1 gap-4">

                                {jobs.map((job) => (

                                    <div

                                        key={job.id}

                                        className="border rounded-lg p-4"

                                    >

                                        <div className="flex items-center justify-between">

                                            <div>

                                                <p className="font-semibold">

                                                    {job.title}

                                                </p>

                                                <p className="text-sm text-muted-foreground">

                                                    {job.company}

                                                </p>

                                            </div>

                                            <Badge>

                                                {job.location}

                                            </Badge>

                                        </div>

                                    </div>
                                ))}

                            </div>

                        </CardContent>

                    </Card>

                    {/* ---------------- */}
                    {/* MATCHES */}
                    {/* ---------------- */}

                    {selectedCV && (

                        <Card>

                            <CardContent className="p-6 space-y-4">

                                <h2 className="text-2xl font-semibold">

                                    Top Matches

                                </h2>

                                <div className="space-y-4">

                                    {matches.map((match) => (

                                        <div

                                            key={match.job_id}

                                            className="border rounded-lg p-4 space-y-3"

                                        >

                                            <div className="flex items-center justify-between">

                                                <div>

                                                    <p className="font-semibold">

                                                        {match.title}

                                                    </p>

                                                    <p className="text-sm text-muted-foreground">

                                                        {match.company}

                                                    </p>

                                                </div>

                                                <Badge>

                                                    {(match.final_score * 100).toFixed(0)}%
                                                    Match

                                                </Badge>

                                            </div>

                                            <p className="text-sm leading-relaxed text-muted-foreground">

                                                {match.reasoning}

                                            </p>

                                        </div>
                                    ))}

                                </div>

                            </CardContent>

                        </Card>
                    )}

                </div>

            </div>

        </main>
    )
}