import React, { useEffect, useState } from 'react';
import { withRouter } from 'react-router-dom';
import Board from 'react-trello';
import { boardService } from '../application/services';
import { withAuthorization } from '../auth/auth-hoc';
import { BoardSkeleton } from '../components/BoardSkeleton';
import { Boards } from '../constant/constant';
import { useParams } from 'react-router-dom';

export const BoardPage = withRouter(
    withAuthorization((authUser) => !!authUser)((props) => {
        const [board, setBoard] = useState({
            lanes: [],
        });
        const [loading, setLoading] = useState(false);

        useEffect(() => {
            (async () => {
                setLoading(true);
                await fetchBoard();
                setLoading(false);
            })();
        }, []);
        const url  = useParams();
        const message = url.board;


        const fetchBoard = async () => {
            const data = (await boardService.getBoard(boardId())).val();
            // setBoard(prepareBoard(data));
            const board = Boards.filter(b => b.key == message)
            setBoard(prepareBoard(board[0]))
        };


        // Fill empty properties that are important for Board component
        const prepareBoard = (board) => ({
            ...board,
            lanes: (board?.lanes || []).map((lane) => ({
                ...lane,
                cards: lane?.cards || [],
            })),
        });

        const boardId = () => props.match?.params?.board;

        const handleDataChange = async (data) => await boardService.updateBoard(boardId(), data);

        if (loading) {
            return <BoardSkeleton count={5} />;
        }


        const handleAllocate = () => {
            console.log(board)
            // here take board make a logic and allocate
            setLoading(true)
        }

        return (
            <div className='bg-blue-500  h-full'>
                <Board
                    className={`pt-16 h-4/5 bg-blue-500 `}
                    canAddLanes={true}
                    editable={true}
                    data={{
                        lanes: board.lanes || [],
                    }}
                    onDataChange={handleDataChange}
                />
                <button 
                onClick={handleAllocate}
                className="glass-effect text-white font-semibold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                    ALLOCATE
                </button>
            </div>
        );
    })
);
