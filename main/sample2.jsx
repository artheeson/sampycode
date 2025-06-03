"use client"
import { useState, useEffect } from "react";

export default function sample2(){
    const [imgUrl, setImgUrl] = useState(null);

    async function fetchDogPhoto() {
        try {
            const res = await fetch("https://dog.ceo/api/breeds/image/random");
            const data = await res.json();
            setImgUrl(data.message); 
        } catch (error) {
            console.error("Error fetching dog image:", error);
        }
    }

    useEffect(() => {
        fetchDogPhoto();
    }, []);

    return (
        <div className="flex min-h-screen items-center justify-center bg-gray-100">
            <div className="flex flex-col items-center">
                {imgUrl && (
                    <img 
                        src={imgUrl}
                        alt="random dog"
                        className="rounded-lg shadow-lg m-2 p-2 w-64 h-64 object-cover"
                    />
                )}
                <button 
                    onClick={fetchDogPhoto} 
                    className="bg-green-500 hover:bg-green-600 text-white rounded p-2 m-2 text-xl"
                >
                    Next Dog
                </button>
            </div>
        </div>
    );
}
