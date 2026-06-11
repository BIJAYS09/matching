"use client"

import {

    useState

} from "react"

import api from "@/lib/api"

import {

    Card,
    CardContent

} from "@/components/ui/card"

import {

    Button

} from "@/components/ui/button"


type Props = {

    onUploadSuccess: (
        cvId: number
    ) => void
}


export default function UploadCV({

    onUploadSuccess

}: Props) {

    const [file, setFile] = useState<File | null>(null)

    const [loading, setLoading] = useState(false)


    async function uploadCV() {

        if (!file) return

        setLoading(true)

        const formData = new FormData()

        formData.append(
            "file",
            file
        )

        try {

            const response = await api.post(

                "/upload-cv",

                formData,

                {
                    headers: {
                        "Content-Type":
                            "multipart/form-data"
                    }
                }
            )

            onUploadSuccess(
                response.data.cv_id
            )

        } catch (err) {

            console.error(err)

        } finally {

            setLoading(false)
        }
    }


    return (

        <Card>

            <CardContent className="p-6 space-y-4">

                <div className="space-y-1">

                    <h2 className="text-2xl font-semibold">

                        Upload CV

                    </h2>

                    <p className="text-muted-foreground">

                        Upload candidate CV
                        for AI-powered matching.

                    </p>

                </div>

                <input

                    type="file"

                    accept=".pdf"

                    onChange={(e) => {

                        if (
                            e.target.files?.[0]
                        ) {

                            setFile(
                                e.target.files[0]
                            )
                        }
                    }}
                />

                <Button

                    onClick={uploadCV}

                    disabled={
                        !file || loading
                    }
                >

                    {loading
                        ? "Processing..."
                        : "Upload CV"}

                </Button>

            </CardContent>

        </Card>
    )
}