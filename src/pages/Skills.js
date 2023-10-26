import React, { useState } from "react";
import { getUser } from "../application/services/auth";
import { ROUTES } from '../application/constants';
import { useHistory } from "react-router-dom/";

export const NameForm = () => {
    const [name, setName] = useState("");
    const [data,setData] = useState({})
    const [tags ,setTags] = useState([]);
    const [inputValue , setInput] = useState("")
    const history = useHistory();

    const handleSubmit = (e) => {
        setData(
            {
                name:name,
                skills:tags,
                email:getUser()?._delegate?.email
                
            })
            // here 

            history.push(ROUTES.BOARDS);

    }
    

    const onAddteam = () => {
        const tagValue = inputValue;
        setTags([...tags, tagValue]);
        setInput("")
    };
    const onRemoveTag = (index) => {
        const updatedTags = [...tags];
        updatedTags.splice(index, 1);
        setTags(updatedTags);
    };

    return (
        <div className="w-full max-w-md mx-auto p-4 m-24">
            <h1 className="text-2xl mb-4">Name Form</h1>
            <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div className="mb-4">
                    <label htmlFor="name" className="block text-gray-700 text-sm font-bold mb-2">Name:</label>
                    <input
                        type="text"
                        id="name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    />
                </div>
                <p className='text[#303972] font-bold'>Skills</p>
                <div className='flex flex-row mb-2'>
                    <input
                        type="string"
                        className="customLook border h-12 border-gray-300 rounded w-full p-2 resize-none"
                        placeholder='Enter Skills'
                        onChange={(e) => setInput(e.target.value)}
                        value={inputValue}
                        onKeyDown={(e) => {
                            if (e.key === 'Enter') {
                                e.preventDefault();
                                onAddteam();
                            }
                        }}
                    />
                    <button
                        onClick={() => onAddteam()}
                    >+</button>
                </div>
                <div className='mb-4'>
                    {tags.map((tag, index) => (
                        <div key={index} className="inline-flex items-center bg-gray-100 text-gray-700 px-2 py-1 rounded-full mr-2 mt-2">
                            <span className="mr-2">{tag}</span>
                            <button
                                className="text-red-500 hover:text-red-600 focus:outline-none"
                              onClick={() => onRemoveTag(index)}
                            >
                                <svg
                                    className="w-4 h-4 fill-current"
                                    viewBox="0 0 24 24"
                                    xmlns="http://www.w3.org/2000/svg"
                                >
                                    <path
                                        d="M17.292 6.292l-1.415-1.415L12 10.586 7.122 5.707 5.707 7.122 10.586 12l-4.88 4.88 1.415 1.415L12 13.414l4.878 4.88 1.414-1.415L13.414 12l4.878-4.878z"
                                    />
                                </svg>
                            </button>
                        </div>
                    ))}
                </div>
                <div className="text-center">
                    <button
                        type="submit"
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    >
                        Submit
                    </button>
                </div>
            </form>
        </div>
    );
}

