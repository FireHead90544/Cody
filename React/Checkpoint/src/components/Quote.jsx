const Quote = ({text, author}) => {
  return (
    <div className="flex flex-col space-y-4 max-w-7xl">
      <span className="text-4xl font-light text-center text-gray-200">
        "{text}"
      </span>
      <span className="text-2xl font-thin text-center text-gray-300">- {author}</span>
    </div>
  )
}

export default Quote