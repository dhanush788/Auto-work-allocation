import { Button, Input, Modal } from 'antd';
import React, { useState } from 'react';
import PropTypes from 'prop-types';

export const BoardModal = (props) => {
    const { closeModal, action, visible } = props;
    const [boardTitle, setBoardTitle] = useState('');
    const [loading, setLoading] = useState(false);
    const [tags , setTags] = useState([]);
    const [inputValue, setInput] = useState("");    


    const isEmptyText = (text) => !text || !text.trim();

    const handleCreateBoard = async (event) => {
        setLoading(true);
        event.preventDefault();
        if (isEmptyText(boardTitle)) {
            return;
        }
        await action({
            title: boardTitle,
        });
        setBoardTitle('');
        setLoading(false);
    };

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
        <Modal
            title="Add board"
            width="400px"
            visible={visible}
            onCancel={closeModal}
            footer={null}
        >
            <form className={`w-full`} onSubmit={(event) => handleCreateBoard(event)}>
                <Input
                    className={`mb-3`}
                    placeholder="Title"
                    onChange={(event) => setBoardTitle(event.target.value)}
                    value={boardTitle}
                />
                <p className='text[#303972] font-bold'>Team Details</p>
                <div className='flex flex-row mb-2'>
                    <input
                        type="email"
                        className="customLook border h-12 border-gray-300 rounded w-full p-2 resize-none"
                        placeholder='Enter email address of team members'
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
                <Button
                    type="primary"
                    onClick={(event) => handleCreateBoard(event)}
                    loading={loading}
                    disabled={isEmptyText(boardTitle)}
                >
                    Add
                </Button>
            </form>
        </Modal>
    );
};

BoardModal.propTypes = {
    closeModal: PropTypes.func.isRequired,
    action: PropTypes.func.isRequired,
    visible: PropTypes.bool.isRequired,
};
